import { View, Text, TextInput, StyleSheet } from "react-native"

const Register = () => {
    
    return(
        <View>
            <Text>Soy el registro</Text>
            <TextInput placeholder="usuario" style={styles.input}></TextInput>
            <TextInput placeholder="contraseña" style={styles.input}></TextInput>
        </View>
    )
}

const styles = StyleSheet.create({
    input: {
      height: 40,
      margin: 12,
      borderWidth: 1,
      padding: 10,
    },
  });

export default Register