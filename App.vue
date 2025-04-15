<template>
  <div id="app">
    <div class="container">
      <h1 class="text-center my-4">Go-Dek: Jasa Titip Student</h1>

      <!-- Pilihan Negara -->
      <div class="form-group">
        <label for="countryChoice">Pilih Tujuan Pengiriman</label>
        <select v-model="countryChoice" class="form-control" id="countryChoice">
          <option value="germany-to-indonesia">Jerman - Indonesia</option>
          <option value="indonesia-to-germany">Indonesia - Jerman</option>
        </select>
      </div>

      <!-- Pilihan Tanggal -->
      <div class="form-group">
        <label for="departureDate">Pilih Tanggal Keberangkatan</label>
        <input type="date" v-model="departureDate" class="form-control" :disabled="isDateDisabled" />
      </div>

      <!-- Pilihan Provinsi / Bundesland -->
      <div class="form-group" v-if="countryChoice === 'germany-to-indonesia'">
        <label for="bundesland">Pilih Bundesland</label>
        <select v-model="bundesland" class="form-control" :disabled="!availableBundeslands.length">
          <option v-for="(bundesland, index) in availableBundeslands" :key="index" :value="bundesland">{{ bundesland }}</option>
        </select>
      </div>

      <div class="form-group" v-if="countryChoice === 'indonesia-to-germany'">
        <label for="province">Pilih Provinsi</label>
        <select v-model="province" class="form-control" :disabled="!availableProvinces.length">
          <option v-for="(province, index) in availableProvinces" :key="index" :value="province">{{ province }}</option>
        </select>
      </div>

      <!-- Isian Berat -->
      <div class="form-group">
        <label for="weight">Berat (kg)</label>
        <input type="number" v-model="weight" class="form-control" min="1" />
      </div>

      <!-- Isian Nama, No HP, dan Email -->
      <div class="form-group">
        <label for="name">Nama</label>
        <input type="text" v-model="name" class="form-control" />
      </div>
      <div class="form-group">
        <label for="phone">Nomor HP</label>
        <input type="text" v-model="phone" class="form-control" />
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" v-model="email" class="form-control" />
      </div>

      <!-- Tombol Hitung -->
      <button class="btn btn-primary" @click="calculateOrder">Hitung</button>

      <!-- Tabel Rincian Pemesanan -->
      <div v-if="showDetails">
        <h3 class="mt-4">Rincian Pemesanan</h3>
        <table class="table table-bordered">
          <thead>
            <tr>
              <th>Nama Pemesan</th>
              <th>No HP</th>
              <th>Email</th>
              <th>Provinsi/Bundesland</th>
              <th>Berat</th>
              <th>Total Biaya</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{{ name }}</td>
              <td>{{ phone }}</td>
              <td>{{ email }}</td>
              <td>{{ countryChoice === 'germany-to-indonesia' ? bundesland : province }}</td>
              <td>{{ weight }} kg</td>
              <td>{{ totalCost }} EUR</td>
            </tr>
          </tbody>
        </table>

        <!-- Metode Pembayaran -->
        <div>
          <h4>Pembayaran</h4>
          <ul>
            <li>Bank Indonesia: Mandiri - 13100009909090 (Asep Saepul)</li>
            <li>Bank Jerman: Deutsche Bank - DE89 9909 9909 0090 90 (Michael Sumaker)</li>
          </ul>
        </div>

        <!-- Tombol Download dan Konfirmasi -->
        <button class="btn btn-success" @click="downloadReceipt">Download Rincian</button>
        <div class="mt-3">
          <button class="btn btn-success" @click="showClosingModal">Saya Telah Membayar</button>
          <button class="btn btn-danger" @click="showCancelModal">Batalkan Transaksi</button>
        </div>
      </div>
    </div>

    <!-- Modal Pop-up Closing -->
    <div v-if="showClosing" class="modal">
      <div class="modal-content">
        <p>Terimakasih sudah membantu student! Pembayaran anda akan kami verifikasi 1x24 jam.</p>
        <button class="btn btn-primary" @click="closeModal">Tutup</button>
      </div>
    </div>

    <!-- Modal Pop-up Cancel -->
    <div v-if="showCancel" class="modal">
      <div class="modal-content">
        <p>Transaksi dibatalkan!</p>
        <button class="btn btn-primary" @click="closeModal">Tutup</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      countryChoice: 'germany-to-indonesia',
      departureDate: '',
      bundesland: '',
      province: '',
      weight: null,
      name: '',
      phone: '',
      email: '',
      showDetails: false,
      totalCost: 0,
      availableBundeslands: ['Nordrhein Westfalen', 'Baden Wurtemberg'],
      availableProvinces: ['Jawa Barat', 'Jakarta'],
      showClosing: false,
      showCancel: false
    };
  },
  computed: {
    isDateDisabled() {
      if (this.countryChoice === 'germany-to-indonesia') {
        return !(this.departureDate === '2025-04-22' || this.departureDate === '2025-04-28');
      }
      if (this.countryChoice === 'indonesia-to-germany') {
        return !(this.departureDate === '2025-04-20' || this.departureDate === '2025-04-29');
      }
      return false;
    }
  },
  methods: {
    calculateOrder() {
      const costPerKg = 14;
      this.totalCost = this.weight * costPerKg;
      this.showDetails = true;
    },
    downloadReceipt() {
      // Logic to download the receipt (e.g., using libraries like FileSaver)
    },
    showClosingModal() {
      this.showClosing = true;
    },
    showCancelModal() {
      this.showCancel = true;
    },
    closeModal() {
      this.showClosing = false;
      this.showCancel = false;
    }
  }
};
</script>

<style scoped>
.modal {
  display: block;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}
</style>
