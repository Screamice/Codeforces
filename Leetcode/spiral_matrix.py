class Solution:

    def spiralOrder(self, matrix):
        if not matrix: return []
        # Número de filas y columnas en la matriz.
        R, C = len(matrix), len(matrix[0])

        # Matriz de tamaño RxC con todos los valores false para saber las posiciones que ya se recorrieron.
        seen = [[False] * C for _ in matrix]

        #Salida
        answer = []

        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        # Incio.
        r = c = di = 0

        for _ in range(R*C):
            # Se agrega a la salida
            answer.append(matrix[r][c])
            # Se marca como vista esa posición.
            seen[r][c] = True

            cr, cc = r+dr[di], c+dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        
        return answer



matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
         ]

sol = Solution()
print(sol.spiralOrder(matrix))