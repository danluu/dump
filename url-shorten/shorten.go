package main

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"
)

var short2long = make([]string,0)
var nextUrl = 0

func newUrl(response http.ResponseWriter, request *http.Request) {
	if (request.Method == "GET") {
		t, _ := template.ParseFiles("static/index.html")
		t.Execute(response, nil)
	} else if (request.Method == "POST") {
		request.ParseForm()
		longUrl := request.PostFormValue("longurl")
		short2long = append(short2long,longUrl)
		fmt.Println(longUrl)
		fmt.Println(nextUrl)
		nextUrl += 1
	} else {
		http.Error(response, "Method not allowed", 405)
		return
	}
}

func forwardUrl(response http.ResponseWriter, request *http.Request) {
	shortUrl,_ := strconv.Atoi(request.URL.Path[1:]) // Strip leading slash.
	
	if shortUrl < len(short2long) {
		longUrl := short2long[shortUrl]
		http.Redirect(response, request, longUrl, 301)
	} else {
		fmt.Println(short2long)
		fmt.Println(shortUrl)
		http.Error(response, "Short URL doesn't exist", 404)
	}
}

func main() {
	router := mux.NewRouter()

	router.HandleFunc("/",newUrl)
	router.HandleFunc("/{shortUrl}",forwardUrl) // TODO: wrong func

	http.Handle("/", router)
	err := http.ListenAndServe(":9999", nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
