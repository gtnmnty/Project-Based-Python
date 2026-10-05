from unittest import result


class Matrix:
    matrix  =   None
    rows    =   None
    cols    =   None

    def __init__(self, data):
        """Initialize matrix with 2D list data."""
        if not isinstance(data, list):
            raise TypeError("Data must be a list of lists")

        if not data:
            raise ValueError("Matrix cannot be empty")

        for row in data:
            if not isinstance(row, list):
                raise TypeError("Each row must be a list")

        row_length = len(data[0])
        if row_length == 0:
            raise ValueError("Rows cannot be empty")

        for row in data:
            if len(row) != row_length:
                raise ValueError("Rows must have the same length")
            for val in row:
                if isinstance(val, bool) or not isinstance(val, (int, float)):
                    raise TypeError("All elements must be int or float")

        # Defensive copy to prevent external mutation
        self.matrix = [row[:] for row in data]
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

    def __mul__(self, other):
        if isinstance(other, (bool, str)):
            raise TypeError("Not an int or float")

        # Validates if scalar is an int or float then proceeds to multiply
        if isinstance(other, (int, float)):
            res = [
                [self.matrix[i][j] * other for j in range(self.cols)]
                for i in range(self.rows)
            ]
            return Matrix(res)

        # Validates if scalar is an int or float then proceeds to multiply
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Rows must have the same length")

            # Create an empty result grid filled with 0s
            res = [ [0 for _ in range(other.cols)] for _ in range(self.rows) ]

            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        res[i][j] += self.matrix[i][k] * other.matrix[k][j]

            return Matrix(res)

        return TypeError("Other is neither int/float nor a Matrix")

    def __rmul__(self, other):
        #Right-hand scalar multiplication (scalar * matrix).
        if isinstance(other, bool):
            return NotImplemented
        if isinstance(other, (int, float)):
            return self * other  # delegate to __mul__
        return NotImplemented


def main():
    # print("=" * 60)
    # print("MATRIX CLASS DEMONSTRATION")
    # print("=" * 60)

    print("——————————————— Test 1: Creating Matrices ———————————————")

    # 2x3 matrix
    matrix_a_data = [[1,2,3.565], [4,5,6]]
    matrix_a = Matrix(matrix_a_data)
    #matrix_a_data[0][0] = "oops"

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

    if matrix_a.rows == matrix_b.rows and matrix_a.cols == matrix_b.cols:
        result_add = matrix_a + matrix_b
        print(f"Result:\n{result_add}")
    else:
        print("Error: Matrices have different dimensions and cannot be added")

    print("————————————— Test 3: Scalar Multiplication —————————————")

    scalar = 2
    result_scalar = matrix_a * scalar
    print(f"Result:\n{result_scalar}")

    print("————————————— Test 4: Matrix Multiplication —————————————")

    if matrix_a.cols == matrix_c.rows:
        result_mult = matrix_a * matrix_c
        print(f"Result:\n{result_mult}")
    else:
        print(f"Error: Cannot multiply {matrix_a.rows}x{matrix_a.cols} by {matrix_c.rows}x{matrix_c.cols}")

    print("——————————————————— Test 5: Transpose ———————————————————")

    result_transpose = matrix_a.transpose()
    print(f"Result:\n{result_transpose}")

    print("————————————— Test 6: Incompatible Addition —————————————")

    try:
        # Try to add matrices with different dimensions
        matrix_d_data = [[1, 2], [3, 4], [5, 6]]  # 3x2
        matrix_d = Matrix(matrix_d_data)

        if matrix_a.rows == matrix_d.rows and matrix_a.cols == matrix_d.cols:
            result_error = matrix_a + matrix_d
            print(f"Result:\n{result_error}")
        else:
            print(f"Error: Cannot add {matrix_a.rows}x{matrix_a.cols} by {matrix_d.rows}x{matrix_d.cols}")
            print("Matrices must have the same dimensions for addition")
    except ValueError as e:
        print(f"Caught expected error: {e}")

    print("—————————— Test 7: Incompatible Multiplication ——————————")

    try:
        matrix_e_data = [[1, 2], [3, 4]]  # 2x2
        matrix_e = Matrix(matrix_e_data)

        if matrix_a.cols == matrix_e.rows:
            result_error = matrix_a * matrix_e
            print(f"Result:\n{result_error}")
        else:
            print(f"Error: Cannot multiply {matrix_a.rows}x{matrix_a.cols} by {matrix_e.rows}x{matrix_e.cols}")
            print(f"Matrix A columns ({matrix_a.cols}) != Matrix E rows ({matrix_e.rows})")
    except ValueError as e:
        print(f"Caught expected error: {e}")

    print("—————————————— Test 8: 2x2 Matrix Inverse ———————————————")

    # Create a 2x2 matrix
    matrix_f_data = [[4, 7], [2, 6]]
    matrix_f = Matrix(matrix_f_data)

    print(f"Original 2x2 Matrix:\n{matrix_f}")

    # Calculate determinant
    a, b = matrix_f.matrix[0]
    c, d = matrix_f.matrix[1]
    determinant = a * d - b * c

    if determinant == 0:
        print("Error: Matrix is singular (determinant is 0), cannot compute inverse")
    else:
        # Calculate inverse
        inverse_data = [
            [d / determinant, -b / determinant],
            [-c / determinant, a / determinant]
        ]
        matrix_f_inverse = Matrix(inverse_data)
        print(f"\nInverse:\n{matrix_f_inverse}")

        # Verify: A * A^(-1) should equal Identity matrix
        identity = matrix_f * matrix_f_inverse
        print(f"\nA * A^(-1) (should be close to identity):\n{identity}")

if __name__ == "__main__":
    main()