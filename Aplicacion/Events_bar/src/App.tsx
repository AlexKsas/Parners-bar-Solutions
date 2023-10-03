import React from 'react';
import { StyleSheet, Text, View, } from 'react-native';
import Login from './components/Login/login';
import register from './components/register/register';


const App = () => {

  return (
    <View style={styles.container}>
      <Text></Text>
      <Login/>
    </View>
  );

}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white', // Cambia este valor al color que desees
    // Otros estilos para el contenedor si es necesario
  },
});

export default App;
