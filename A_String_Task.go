package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	s, _ := r.ReadString('\n')
	s = strings.TrimSpace(s)
	s = strings.ToLower(s)

	vowels := map[rune]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'y': true}
	parts := make([]string, 0, len(s))
	for _, r := range s {
		if !vowels[r] {
			parts = append(parts, string(r))
		}
	}

	fmt.Println("." + strings.Join(parts, "."))
}
