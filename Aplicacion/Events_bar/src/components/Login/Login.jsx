import { View, Text, TextInput, StyleSheet, Button, TouchableOpacity} from 'react-native';
import Desing from '../Diseno/Desing';
import { useNavigation } from '@react-navigation/native';
import { Component } from 'react';



function Login (){
    const navigation = useNavigation();
    return(
        <View style={Desing.inicio}>

            <Text style={Desing.text}></Text>

            <TextInput placeholderTextColor={"lightgray"} placeholder="USUARIO" style={Desing.input}></TextInput>
            <TextInput placeholderTextColor={"lightgray"} placeholder="CONTRASEÑA" style={Desing.input}></TextInput>

            <TouchableOpacity style={Desing.button} onPress={() => navigation.navigate('Inicio')}>
                <Text style={Desing.buttonText}>Ingresar</Text>
            </TouchableOpacity>           
            
            <TouchableOpacity style={Desing.button} onPress={() => navigation.navigate("Persona")}>
                <Text style={Desing.buttonText}>Registrar</Text>
            </TouchableOpacity>

            <TouchableOpacity style={Desing.button} onPress={() => navigation.navigate("RestablecerContrasena")} >
                <Text style={Desing.buttonText}>Recuperar Contraseña</Text>
            </TouchableOpacity>

        </View>
    )
}

export default Login