import React from 'react';
import { View, Text, FlatList } from 'react-native';

const data = [
  { id: 1, evento: 'Concierto en vivo', hora: '19:00', precio: '$30.00' },
  { id: 2, evento: 'Feria de comida', hora: '14:00', precio: '$10.00' },
];
const Login = () => {
    return (
      <View>
        <Text style={{ fontSize: 24, fontWeight: 'bold', margin: 20, color:"black"}}>
          Eventos y Precios
        </Text>
        <FlatList
          data={data}
          keyExtractor={(item) => item.id.toString()}
          renderItem={({ item }) => (
            <View style={{ margin: 10 }}>
              <Text style={{ fontSize: 18, fontWeight: 'bold', color:"black" }}>{item.evento}</Text>
              <Text style={{color:"black"}} >Hora: {item.hora}</Text>
              <Text style={{color:"black"}} >Precio: {item.precio}</Text>
            </View>
          )}
        />
      </View>
    );
  };
  
  export default Login;