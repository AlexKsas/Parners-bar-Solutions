import { View, Text, TextInput, StyleSheet, Button, TouchableOpacity} from 'react-native';
import Desing from '../Diseno/Desing';
import { useNavigation } from '@react-navigation/native';
import { Component } from 'react';



function Login (){
    const navigation = useNavigation();
    return(
        <View style={Desing.inicio}>
            <Text style={[Desing.text, styles.title]}>Ingresar Usuario</Text>
                <TextInput placeholderTextColor={"lightgray"} placeholder="USUARIO" style={Desing.input} underlineColorAndroid="transparent"/>
                <TextInput placeholderTextColor={"lightgray"} placeholder="CONTRASEÑA" style={Desing.input} 
                secureTextEntry={true} underlineColorAndroid="transparent" />
            <View style={[styles.viewRestablecer]}>
                <TouchableOpacity onPress={() => navigation.navigate("RestablecerContrasena")}>
                    <Text style={styles.textRestablecer}>Restablecer Contraseña</Text>
                </TouchableOpacity>
            </View>
            

            <TouchableOpacity style={Desing.button} onPress={() => navigation.navigate('Inicio')}>
                <Text style={Desing.buttonText}>Entrar</Text>
            </TouchableOpacity>
            
            <TouchableOpacity style={Desing.button} onPress={() => navigation.navigate("InicioRegistrar")}>
                <Text style={Desing.buttonText}>Registrar</Text>
            </TouchableOpacity>


        </View>
    )
}
const styles = StyleSheet.create({
    title:{
        color:'gray'
    },
    textRestablecer:{
        color:'blue',
        textAlign:'right'
    },
    viewRestablecer:{
        width:'70%',
        marginTop:-10
    }

})
export default Login