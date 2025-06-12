from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]  # Baris pertama (indeks 0)

        for i in range(1, rowIndex + 1):
            # Sisipkan 0 di awal dan akhir untuk perhitungan kombinasi
            row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]

        return row
