import React from 'react';
import { StyleSheet, Text, View, } from 'react-native';
import Persona from './components/Register/Persona';
import Establecimiento from './components/Register/Establecimiento';
import Inicio from './components/Register/Inicio';
import { NavigationContainer } from '@react-navigation/native';
import {   createStackNavigator } from '@react-navigation/stack';
import Home from './components/Home/Home';
import Login from './components/Login/Login';
import RestablecerContrasena from './components/RestablecerContrasena/RestablecerContrasena';
import Menu from './menu/Menu';
import InicioUser from './components/Inicio/InicioUser';



const Stack = createStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen name="Login" component={Login} options={{headerShown:false}} />
        <Stack.Screen name="InicioRegistrar" component={Inicio} options={{headerShown:false}} />
        <Stack.Screen name="RegistrarUsuario" component={Persona} options={{headerTitle:"Persona"}} />
        <Stack.Screen name="RegistrarEstablecimiento" component={Establecimiento} options={{headerTitle:"Establecimiento"}} />
        <Stack.Screen name="Inicio" component={Menu} options={{headerShown:false}} />
        <Stack.Screen name="RestablecerContrasena" component={RestablecerContrasena} options={{headerTitle:"Restablecer Contraseña"}} />
        <Stack.Screen name="InicioUser" component={InicioUser} options={{headerTitle:"Inicio Usuario"}} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
