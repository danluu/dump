package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/sessions"
)

// Authorization Key
var authKey = []byte("somesecret")

// Encryption Key
var cryptKey = []byte("someothersecret")

var store = sessions.NewCookieStore(authKey, cryptKey)

func initSession(request *http.Request) *sessions.Session {
	session, _ := store.Get(request, "wat_cookie") // TODO: handle error.
	if session.IsNew {
		session.Options.Domain = ""       // TODO: set domain.
		session.Options.MaxAge = 3600 * 8 // 8 hours.
		session.Options.HttpOnly = true
		session.Options.Secure = false
	}
	return session
}

func pageWithSession(writer http.ResponseWriter, request *http.Request) {
	session := initSession(request)
	session.Values["page"] = "view"
	session.Save(request, writer)
	fmt.Println("Attempted to make session cookie")
}

func main() {
	http.HandleFunc("/", pageWithSession)

	err := http.ListenAndServe(":9999", nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
