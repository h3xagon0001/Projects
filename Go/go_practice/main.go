package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"math/rand"
	"os"
)

func ping(name string) (string, error) {
	if name == "" {
		return "", errors.New("Need someone to ping, empty strings not allowed.")
	}

	response := fmt.Sprintf("@%v", name)
	return response, nil
}

func menu() (choice int, err error) {
	menuText := "----------------" + "\n" +
		"[0] Exit" + "\n" +
		"[1] Bubble sort" + "\n" +
		"[2] Calculator" + "\n" +
		"[3] Create and write file" + "\n" +
		"Select an option: "

	fmt.Print(menuText)

	_, err = fmt.Scanln(&choice)
	if err != nil {
		return -1, err
	}
	return choice, nil

}

func bubbleSort() (err error) {
	var length int

	fmt.Print("Length: ")
	_, err = fmt.Scanln(&length)
	if err != nil {
		log.Fatal(err)
	}

	if length < 0 {
		return errors.New("Slice cannot have negative length.")
	}

	nums := make([]int, length)
	swaps := 0

	for i := range nums {
		nums[i] = rand.Intn(length * 2)
	}

	fmt.Println(nums)

	for iteration := range nums {
		isSorted := true

		for i := 0; i < length-iteration-1; i++ {
			if nums[i] > nums[i+1] {
				swaps++
				isSorted = false

				temp := nums[i]
				nums[i] = nums[i+1]
				nums[i+1] = temp
			}

			for x := range nums {
				if i+1 == x {
					fmt.Printf("[%d] ", nums[x])
				} else {
					fmt.Printf("%d  ", nums[x])
				}
			}

			fmt.Println()
		}

		if isSorted {
			break
		}
	}

	println("Swaps: ", swaps)
	return nil
}

func calc() (err error) {
	var num1, num2 float64
	var operator string

	fmt.Print("Num 1: ")
	_, err = fmt.Scanln(&num1)
	if err != nil {
		return err
	}

	fmt.Print("Num 2: ")
	_, err = fmt.Scanln(&num2)
	if err != nil {
		return err
	}

	fmt.Print("Operator (+, -, *, /): ")
	_, err = fmt.Scanln(&operator)
	if err != nil {
		return err
	}

	switch operator {
	case "+":
		fmt.Println(num1 + num2)
	case "-":
		fmt.Println(num1 - num2)
	case "*":
		fmt.Println(num1 * num2)
	case "/":
		fmt.Println(num1 / num2)
	default:
		fmt.Println("Invalid operator.")
	}

	return nil
}

func writeFile() (err error) {
	var filename string
	var choice string

	fmt.Print("Filename: ")
	_, err = fmt.Scanln(&filename)
	if err != nil {
		return err
	}

	file, err := os.Open(filename)

	if os.IsNotExist(err) {
		file, _ = os.Create(filename)
		err = nil
	} else {
		fmt.Printf("Overwrite %v? (y/n): ", filename)
		_, err = fmt.Scanln(&choice)
		if err != nil {
			return err
		}

		switch choice {
		case "y":
			file, _ = os.Create(filename)
		case "n":
			return nil
		default:
			fmt.Println("Invalid choice.")
			return nil
		}
	}

	fmt.Print("Write to file: ")
	stdin := bufio.NewReader(os.Stdin)
	content, err := stdin.ReadBytes('\n')
	if err != nil {
		return err
	}

	_, err = file.Write(content)
	if err != nil {
		return err
	}

	file.Close()

	return nil
}

func main() {
	fmt.Println("[Go Practice Program]")

	for {
		choice, err := menu()
		if err != nil {
			if err.Error() != "unexpected newline" {
				log.Fatal(err)
			}
		}

		switch choice {
		case 0:
			fmt.Println("Exiting program.")
			return

		case 1:
			err = bubbleSort()
			if err != nil {
				log.Fatal(err)
			}

		case 2:
			err := calc()
			if err != nil {
				log.Fatal(err)
			}

		case 3:
			err := writeFile()
			if err != nil {
				log.Fatal(err)
			}

		default:
			fmt.Println("Invalid choice.")
		}
	}
}
