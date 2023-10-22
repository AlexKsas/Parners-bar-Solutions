import React from 'react';
import { StyleSheet, Text, View, } from 'react-native';
import Persona from './components/Register/Persona';
import Establecimiento from './components/Register/Establecimiento';
import Inicio from './components/Register/Inicio';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Home from './components/Home/Home';
import Login from './components/Login/Login';
import RestablecerContrasena from './components/RestablecerContrasena/RestablecerContrasena';



const Stack = createStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen name="Login" component={Login} />
        <Stack.Screen name="InicioRegistrar" component={Inicio} />
        <Stack.Screen name="RegistrarUsuario" component={Persona} />
        <Stack.Screen name="RegistrarEstablecimiento" component={Establecimiento} />
        <Stack.Screen name="Inicio" component={Home} />
        <Stack.Screen name="RestablecerContrasena" component={RestablecerContrasena} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
  },
});

export default App;
