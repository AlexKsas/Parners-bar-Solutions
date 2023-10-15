import React from 'react';
import { StyleSheet, Text, View, } from 'react-native';
import Login from './components/Login/login';
<<<<<<< HEAD
import register from './components/register/register';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();
=======
import Register from './pages/Register/Register';


>>>>>>> 84e97d621a65fbe1962df44b6e7800b6529e3ad0

function App() {
  return (
        <React.Fragment>
          <Register />
        </React.Fragment>

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
