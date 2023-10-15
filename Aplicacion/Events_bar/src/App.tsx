import React from 'react';
import { StyleSheet, Text, View, } from 'react-native';
import Login from './components/Login/login';
import Register from './pages/Register/Register';



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
