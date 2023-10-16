import React from 'react';
import { StyleSheet, Text, View, } from 'react-native';
import Login from './components/Login/login';
import Persona from './components/Register/Persona';
import Establecimiento from './components/Register/Establecimiento';
import Inicio from './components/Register/Inicio';


function App() {
  return (
    <React.Fragment>
      {/* <Persona /> */}
      <Establecimiento />
      {/* <Inicio/> */}
    </React.Fragment>
  );
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
  },
});

export default App;
