package main

import (
	"net/http"

	"github.com/gorilla/mux"
)

func main() {
	go globalHub.run()

	r := mux.NewRouter()

	r.PathPrefix("/").Handler(http.FileServer(http.Dir("./static/")))
	http.HandleFunc("/echo",wsHandler)
	http.Handle("/", r)

	// wait for clients
	http.ListenAndServe(":9999", nil)
}
