package main

import (
	"fmt"
	"html/template"
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

func loginUrl(response http.ResponseWriter, request *http.Request) {
	if request.Method == "GET" {
		t, _ := template.ParseFiles("static/index.html")
		t.Execute(response, nil)
	} else if request.Method == "POST" {
		request.ParseForm()
		username := request.PostFormValue("username")
		fmt.Println("Username: ", username)

		session := initSession(request)
		userId, ok := session.Values["userId"].(string)
		if ok {
			// Already has username. This section for debugging only.
			fmt.Println("Changing username %v : %v", userId, username)
		}

		session.Values["userId"] = username
		err := session.Save(request, response)
		if err != nil {
			log.Fatal("session.Save: ", err)
		}

		// Can't redirect from here.
		http.Redirect(response, request, "localhost:9999/play", 301)
	} else {
		http.Error(response, "Method not allowed", 405)
		return
	}
}

func main() {
	http.HandleFunc("/", loginUrl)

	err := http.ListenAndServe(":9999", nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
