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
      backgroundColor: 'transparent', // Color de fondo transparente
      padding: 10,
      borderRadius: 40,
      margin: 15,
      elevation: 5, // Agrega elevación para dar un aspecto de relieve en dispositivos Android
      shadowColor: 'rgba(255, 100, 0, 0.8)', // Color de sombra
      shadowOffset: { width: 0, height: 3 }, // Desplazamiento de sombra (eje X, eje Y)
      shadowRadius: 5, // Radio de la sombra
      shadowOpacity: 0.5, // Opacidad de la sombra
    },
    buttonText: {
      color: 'rgba(255, 100, 0, 0.8)', // Color de texto en azul
      textAlign: 'center',
      fontSize: 16,
      fontWeight: 'bold',
      textTransform: 'uppercase',
      padding: 10,
      borderRadius: 40,
      backgroundColor: 'white', // Color de fondo blanco
    },
    
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: 'darkslateblue'
    }
  });

  export default Desing