package main

import (
	"fmt"
	"github.com/gorilla/mux"
	"net/http"
)

func HomeHandler(response http.ResponseWriter, request *http.Request) {
	fmt.Fprintf(response, "Hello, world!\n")
}

func main() {
	r := mux.NewRouter()

	r.PathPrefix("/").Handler(http.FileServer(http.Dir("./static/")))
	http.Handle("/", r)

	// wait for clients
	http.ListenAndServe(":9999", nil)
}
