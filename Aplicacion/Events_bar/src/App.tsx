import React from 'react';
import { StyleSheet, Text, View, } from 'react-native';
import Login from './components/Login/login';
import register from './components/register/register';


import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Login" component={Login} />
        <Stack.Screen name="Register" component={register} />
      </Stack.Navigator>
    </NavigationContainer>
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
