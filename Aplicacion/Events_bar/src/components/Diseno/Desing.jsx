import { View, Text, TextInput, StyleSheet, Button, TouchableOpacity} from "react-native"


// Diseño de la interfaz de login
const Desing = StyleSheet.create({
    inicio:{
      flex: 1,
      justifyContent: 'center', // Centrar verticalmente
      alignItems: 'center',
    },

    input: {
      height: 40,
      width: '80%', // Ancho del input
      paddingHorizontal: 10,
      borderRadius: 10, // Bordes redondeados
      borderWidth: 1,
      borderColor: 'gray',
      margin:25,
      color:'black',

    },
    text: {
      textAlign: 'center',
      color: 'white', // Cambiado a azul para generar un estilo más fresco
      fontSize: 28, // Tamaño de fuente aumentado
      fontWeight: 'bold',
      marginBottom: 20,
    },
    button: {
      backgroundColor: 'white',
      padding: 10,
      borderRadius: 5,
      margin:25,
    
    },
    buttonText: {
      color: 'white',
      textAlign: 'center',
      fontSize: 16, // Tamaño de fuente
      fontWeight: 'bold', // Peso de fuente (negrita)
      textTransform: 'uppercase', // Transformación de texto a mayúsculas
      padding: 10, // Espaciado interno
      backgroundColor: 'blue', // Color de fondo
      borderRadius: 5, // Bordes redondeados
    },
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
    }
  });

  export default Desing