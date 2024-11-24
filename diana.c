#include <stdio.h>

// Sub-program untuk menghitung total
float HitungTotal(int n) {
    float total = 0;
    float number;
    for (int count = 0; count < n; count++) {
        printf("Masukkan angka ke-%d: ", count + 1);
        scanf("%f", &number);
        total += number;
    }
    return total;
}

// Sub-program untuk menghitung rata-rata
float HitungRataRata(float total, int n) {
    return total / n;
}

int main() {
    int n;
    float total, average;

    // Meminta input jumlah angka yang ingin dimasukkan
    printf("Masukkan jumlah angka yang ingin dihitung: ");
    scanf("%d", &n);

    // Mengecek jika n valid (lebih besar dari 0)
    if (n <= 0) {
        printf("Jumlah angka harus lebih besar dari 0.\n");
        return 1;  // Keluar dari program jika n tidak valid
    }

    // Menghitung total dan rata-rata
    total = HitungTotal(n);
    average = HitungRataRata(total, n);

    // Menampilkan hasil rata-rata
    printf("Total angka yang dimasukkan: %.2f\n", total);
    printf("Rata-rata adalah: %.2f\n", average);

    return 0;
}
