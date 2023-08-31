import React from 'react';
import { Text, View, } from 'react-native';
import Register from './components/Register/register';
import Login from './components/Login/login';

const App = () => {

  return (
    <View>
      <Text>Hola mundo</Text>
      <Register/>
      <Login/>
    </View>
  );

}

export default App;
