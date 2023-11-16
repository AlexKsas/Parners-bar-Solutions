import React, { useState } from 'react';
import { View, Text, TextInput, StyleSheet, Button, TouchableOpacity, KeyboardAvoidingView, ScrollView} from 'react-native';
import Desing from '../Diseno/Desing';


const Login = () => {
    const [passwordVisible, setPasswordVisible] = useState(false);
    const [password, setPassword] = useState('');

    const togglePasswordVisibility = () => {
    setPasswordVisible(!passwordVisible);
  };
    return(
        
        <ScrollView contentContainerStyle={Desing.container} >

            <Text style={Desing.text}></Text>

            <TextInput placeholderTextColor={"lightgray"} placeholder="USUARIO" style={Desing.input}></TextInput>
            <TextInput placeholderTextColor={"lightgray"} placeholder="CONTRASEÑA" style={Desing.input} secureTextEntry={!passwordVisible}value={password}onChangeText={(text) => setPassword(text)}></TextInput>
            

            <TouchableOpacity style={Desing.button}>
            <Text style={Desing.buttonText}>Ingresar</Text>
            </TouchableOpacity>
            
            <TouchableOpacity style={Desing.button}>
            <Text style={Desing.buttonText}>Registrar</Text>
            </TouchableOpacity>

            <TouchableOpacity style={Desing.button}>
            <Text style={Desing.buttonText}>Recuperar Contraseña</Text>
            </TouchableOpacity>

        </ScrollView>
        
    )
}

export default Login