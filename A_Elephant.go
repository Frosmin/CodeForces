package main

import "fmt"

func main() {
	var res int
	var numero int
	fmt.Scan(&numero)
	for numero > 0 {
		if numero >= 5 {
			res++
			numero = (numero - 5)
		} else if numero == 4 {
			res++
			numero = numero - 4
		} else if numero == 3 {
			res++
			numero = numero - 3
		} else if numero == 2 {
			res++
			numero = numero - 2
		} else if numero == 1 {
			res++
			numero = numero - 1
		}
	}
	fmt.Print(res)
}
