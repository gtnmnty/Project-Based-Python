
class Matrix:
    matrix  =   None
    rows    =   None
    cols    =   None

    def __init__(self, data):
        # Validates if data is a list type
        if not isinstance(data, list):
            raise TypeError("Data must be a list of lists")

        # Validates if data is not empty
        if not data:
            raise ValueError("Matrix cannot be empty")

        # Validates every row if is a list/
        for row in data:
            if not isinstance(row, list):
                raise TypeError("Row must be a list")

        # Validates the length of every row in the data
        row_length = len(data[0])
        for row in data:
            if len(row) != row_length:
                raise ValueError("Rows length must be the same")
            for val in row:
                if not isinstance(val, (int, float)):
                    raise TypeError("Values must be either an int or float")

        self.matrix = data
        self.rows = len(data)
        self.cols = row_length

    # Readable string representation
    def __repr__(self):
        str_row = []
        for row in self.matrix:
            str_row.append("[" + ",".join(
                f"{val:.2f}" if isinstance(val, float) else f"{val:3}"
                for val in row
            ) + " ]")
        return f"Matrix([\n" + "\n".join(str_row) + "\n])"

    # Friendly representation version
    # def __str__(self):
    #     str_row = []
    #     for row in self.matrix:
    #         str_row.append("[" + ",".join(
    #             f"{val:.2f}" if isinstance(val, float) else f"{val:4}"
    #             for val in row
    #         ) + " ]")
    #     return "\n".join(str_row)

    def transpose(self):
        res = [
            [self.matrix[i][j] for i in range(self.rows)]
            for j in range(self.cols)
        ]

        return Matrix(res)   # New Matrix instance

    def __add__(self, other):
        # Validate if the other is Matrix as well
        if not isinstance(other, Matrix):
            # raise NotImplemented is more advanced due to it
            # tells Python to try other options before stopping/giving up
            raise TypeError("Not a matrix")

        # Validate the length of both rows and cols first
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")

        # Add the values by their index
        res = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]

        # Return the final result
        return Matrix(res)



def main():
    # print("=" * 60)
    # print("MATRIX CLASS DEMONSTRATION")
    # print("=" * 60)

    print("——————————————— Test 1: Creating Matrices ———————————————")

    # 2x3 matrix
    matrix_a_data = [[1,2,3.565], [4,5,6]]
    matrix_a = Matrix(matrix_a_data)
    matrix_a_data[0][0] = "oops"

    # Another 2x3 matrix
    matrix_b_data = [[7, 8, 9], [10, 11, 12]]
    matrix_b = Matrix(matrix_b_data)

    # 3x2 matrix for multiplication
    matrix_c_data = [[1, 2], [3, 4], [5, 6]]
    matrix_c = Matrix(matrix_c_data)

    #Displays the output
    print(f"Matrix A (2x3):\n{matrix_a}")
    print(f"\nMatrix B (2x3):\n{matrix_b}")
    print(f"\nMatrix C (3x2):\n{matrix_c}")

    print("—————————————————————— Test 2: Add ——————————————————————")


    print("————————————— Test 3: Scalar Multiplication —————————————")


    print("————————————— Test 4: Matrix Multiplication —————————————")


    print("——————————————————— Test 5: Transpose ———————————————————")


    print("————————————— Test 6: Incompatible Addition —————————————")


    print("—————————— Test 7: Incompatible Multiplication ——————————")


    print("—————————————— Test 8: 2x2 Matrix Inverse ———————————————")


if __name__ == "__main__":
    main()