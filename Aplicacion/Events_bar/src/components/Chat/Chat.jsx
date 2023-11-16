import React, { useState } from "react";
import { Button, ScrollView, StyleSheet, Text, TextInput, View } from "react-native";

const Chat = () => {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([
    { text: "Hola!", isUser: false },
    { text: "¿Cómo estás?", isUser: true },
    { text: "Bien, ¿dónde nos vemos hoy?", isUser: false },
    { text: "Ya estoy buscando el evento", isUser: true },
  ]);

  const handleSend = () => {
    if (message.trim() === "") return;

    setChat([...chat, { text: message, isUser: true }]);
    setMessage("");
  };

  return (
    <View style={styles.container}>
      <ScrollView style={styles.chatContainer}>
        {chat.map((msg, index) => (
          <View key={index} style={msg.isUser ? styles.userMessage : styles.otherMessage}>
            <Text style={styles.messageText}>{msg.text}</Text>
          </View>
        ))}
      </ScrollView>
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.input}
          placeholder="Escribe tu mensaje..."
          value={message}
          onChangeText={(text) => setMessage(text)}
        />
        <Button title="Enviar" onPress={handleSend} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "space-between",
  },
  chatContainer: {
    flex: 1,
    padding: 10,
  },
  userMessage: {
    alignSelf: "flex-end",
    backgroundColor: "#4CAF50",
    padding: 10,
    borderRadius: 8,
    marginBottom: 8,
    maxWidth: "70%",
  },
  otherMessage: {
    alignSelf: "flex-start",
    backgroundColor: "#ddd",
    padding: 10,
    borderRadius: 8,
    marginBottom: 8,
    maxWidth: "70%",
  },
  messageText: {
    color: "#fff",
  },
  inputContainer: {
    flexDirection: "row",
    alignItems: "center",
    padding: 10,
  },
  input: {
    flex: 1,
    marginRight: 10,
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 5,
    padding: 8,
  },
});

export default Chat;
