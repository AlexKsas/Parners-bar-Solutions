import { useState } from "react";
import { View, Text, TextInput, StyleSheet, Alert, TouchableOpacity, ScrollView, Image } from "react-native";

const Establecimiento = () => {

  const [nombre, setNombre] = useState('')
  const [email, setEmail] = useState('')
  const [telefono, setTelefono] = useState('')
  const [direccion, setDireccion] = useState('')

  const handleSubmit = () => {
    Alert.alert(`${nombre}, ${email}, ${telefono}, ${direccion}`)
  }

  return (
    <View style={styles.form}>
      <ScrollView>
        <View>
          <Text style={[styles.label, { marginTop: 50 }]}>Nombre:</Text>
          <TextInput style={styles.input}
            placeholder="ingresar nombre"
            value={nombre}
            onChangeText={setNombre} />
        </View>

        <Text style={styles.label}>Email:</Text>
        <TextInput style={styles.input}
          placeholder="ingresar Email"
          value={email}
          onChangeText={setEmail} />

        <Text style={styles.label}>Telefono:</Text>
        <TextInput style={styles.input}
          placeholder="ingresar Telefono"
          value={telefono}
          onChangeText={setTelefono} />

        <Text style={styles.label}>Direccion:</Text>
        <TextInput style={styles.input}
          placeholder="ingresar Numero de documento"
          value={direccion}
          onChangeText={setDireccion} />

        <TouchableOpacity onPress={handleSubmit} style={styles.submit}>
          <Text style={styles.submitText}>Continuar</Text>
        </TouchableOpacity>
      </ScrollView>
    </View>
  )
}

const styles = StyleSheet.create({
  input: {
    height: 40,
    borderColor: '#4D4C7D',
    backgroundColor: '#F5F5F5',
    marginRight: 'auto',
    marginLeft: "auto",
    width: 280,
    borderRadius: 15
  },
  icon: {
    backgroundColor: "red",
    borderRadius: 25,
    height: 40,
    width: 40
  },
  form: {
    flex: 1,
    backgroundColor: '#363062',
    height: '100%'
  },
  label: {
    fontSize: 20,
    color: '#F5F5F5',
    marginRight: "auto",
    marginLeft: "auto",
    marginBottom: 5,
    marginTop: 25
  },
  submit: {
    backgroundColor: '#F99417',
    marginRight: "auto",
    marginLeft: "auto",
    borderRadius: 15,
    marginTop: 40
  },
  submitText: {
    fontSize: 24,
    alignItems: 'center',
    padding: 10
  }
});

export default Establecimiento
