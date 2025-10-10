package main

import (
	"log"
	"net/http"
	"github.com/gin-gonic/gin"
	"github.com/gorilla/websocket"
)

func main() {
	router := gin.Default()
	router.StaticFile("/", "./static/index.html")
	router.GET("/ws", serveWebsocket)

	// start server on port 1337
	err := router.Run(":1337")

	// if error occurs
	if err != nil {
		log.Fatalf("Unable to start server. Error: %v", err)
	}

	log.Println("Server started successfully.")
}

func serveWebsocket(c *gin.Context) {
	// upgrades http handshake to persistent tcp connection
	upgrader := websocket.Upgrader{CheckOrigin: func(r *http.Request) bool { return true }}
	connection, err := upgrader.Upgrade(c.Writer, c.Request, nil)
	if err != nil {
		log.Printf("Unable to upgrade websocket. Error: %v", err)
		return
	}

	go handleClient(connection)
}

// init a map (key:value pair) of clients
// following websocket.Conn structure (dict)
var clients = make(map[*websocket.Conn]struct{})

type Message struct {
	Username string `json:"username"`
	Message  string `json:"message"`
}

func handleClient(c *websocket.Conn) {
	// always close websocket on successful execution or error of handleClient()
	defer func() {
		delete(clients, c)
		log.Println("Closing websocket.")
		c.Close()
	}()

	// create set of clients
	clients[c] = struct{}{}

	// loop until return
	for {
		var msg Message
		err := c.ReadJSON(&msg)
		if err != nil {
			log.Printf("Error in reading json message. Error: %v", err)
			return
		}

		broadcast(msg)
	}
}

func broadcast(msg Message) {
	for connection := range clients {
		connection.WriteJSON(msg)
	}
}
