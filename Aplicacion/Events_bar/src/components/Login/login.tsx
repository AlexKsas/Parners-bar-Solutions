import { View, Text, TextInput, StyleSheet, Button, TouchableOpacity} from 'react-native';
import Desing from '../Diseno/Desing';

const Login = () => {
    return(
        <View style={Desing.inicio}>

            <Text style={Desing.text}></Text>

            <TextInput placeholderTextColor={"lightgray"} placeholder="USUARIO" style={Desing.input}></TextInput>
            <TextInput placeholderTextColor={"lightgray"} placeholder="CONTRASEÑA" style={Desing.input}></TextInput>

            <TouchableOpacity style={Desing.button}>
            <Text style={Desing.buttonText}>Ingresar</Text>
            </TouchableOpacity>

            <TouchableOpacity style={Desing.button}>
            <Text style={Desing.buttonText}>Registrar</Text>
            </TouchableOpacity>

        </View>
    )
}

export default Login