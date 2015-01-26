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
var cryptKey = []byte("someothersecret!")

var store = sessions.NewCookieStore(authKey, cryptKey)

func initSession(request *http.Request) *sessions.Session {
	session, _ := store.Get(request, "wat_cookie2") // TODO: handle error.
	if session.IsNew {
		session.Options.Domain = "" // TODO: set domain.
		session.Options.MaxAge = 10 // 10 seconds for debugging.
		session.Options.Path = "/"
		session.Options.HttpOnly = true
		session.Options.Secure = true
	}
	return session
}

func pageWithSession(writer http.ResponseWriter, request *http.Request) {
	session := initSession(request)

	userId, ok := session.Values["user"].(string)
	if !ok {
		// Never seen the user before or some weirdo error.
		userId = "watwatwat"
	}
	fmt.Println("Exiting user id: ", userId)

	session.Values["user"] = userId + " 1"
	err := session.Save(request, writer)
	if err != nil {
		log.Fatal("session.Save: ", err)
	}
	fmt.Println("Attempted to make session cookie")
}

func main() {
	http.HandleFunc("/", pageWithSession)

	err := http.ListenAndServe(":9999", nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
