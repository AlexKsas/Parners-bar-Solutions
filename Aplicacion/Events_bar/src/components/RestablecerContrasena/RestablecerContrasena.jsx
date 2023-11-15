import React, { Component, PureComponent, useState } from 'react'
import {View, StyleSheet, Text, TextInput, Button } from 'react-native'
import firebase from '@react-native-firebase/app';
import '@react-native-firebase/auth';

const firebaseConfig = {
    apiKey: "AIzaSyDhzyF7V7-uvGEVJLlcyX_Awb6B5Xx9CnQ",
    authDomain: "event-bar.firebaseapp.com",
    databaseURL: "https://event-bar-default-rtdb.firebaseio.com",
    projectId: "event-bar",
    storageBucket: "event-bar.appspot.com",
    messagingSenderId: "367568135817",
    appId: "1:367568135817:web:51a63f16d96d19d5c04858",
    measurementId: "G-ZLYS3CCV6H"
  };
  
  if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
  }

function RestablecerContrasena() {
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');
  
    const handleResetPassword = () => {
      firebase
        .auth()
        .sendPasswordResetEmail(email)
        .then((mensaje) => {
            console.log("mensaje ", mensaje)
          setMessage('Se ha enviado un enlace para restablecer la contraseña a tu correo electrónico.');
        })
        .catch(error => {
            console.log(`Error: ${error.message}`)
            setMessage(`Error: ${error.message}`);
        });
    };
  
    return (
      <View style={styles.container}>
        <Text style={styles.title}>Restablecer Contraseña</Text>
        <TextInput
          style={styles.input}
          placeholder="Correo Electrónico"
          placeholderTextColor={'gray'}
          value={email}
          onChangeText={text => setEmail(text)}
        />
        <Button title="Enviar enlace de restablecimiento" onPress={handleResetPassword} />
        {message !== '' && <Text style={styles.message}>{message}</Text>}
      </View>
    );
  }
  
  export default RestablecerContrasena;

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#f0f0f0',
    },
    title: {
      fontSize: 24,
      fontWeight: 'bold',
      marginBottom: 20,
      color:'gray'
    },
    input: {
      width: '80%',
      height: 40,
      borderColor: 'gray',
      borderWidth: 1,
      borderRadius: 5,
      paddingLeft: 10,
      marginBottom: 10,
      color:'black'
    },
    message: {
      color: 'red',
      marginBottom: 10,
    },
  });
  