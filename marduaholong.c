#include <stdio.h>

// Fungsi untuk menghitung luas jajar genjang
float hitungLuasJajarGenjang(float alas, float tinggi) {
    return alas * tinggi;
}

int main() {
    // Nilai yang sudah dimasukkan
    float alas = 10.0;  // Misalnya panjang alas = 10.0
    float tinggi = 5.0; // Misalnya tinggi = 5.0
    float luas;

    // Menghitung luas menggunakan fungsi
    luas = hitungLuasJajarGenjang(alas, tinggi);

    // Output hasil luas
    printf("Luas jajar genjang dengan alas %.2f dan tinggi %.2f adalah: %.2f\n", alas, tinggi, luas);

    return 0;
}
