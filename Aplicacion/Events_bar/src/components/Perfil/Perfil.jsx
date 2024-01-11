import React from "react";
import { StyleSheet, Text, View, Image, ScrollView, TouchableOpacity } from "react-native";
import { useNavigation } from '@react-navigation/native';


const Profile = () => {
  const navigation = useNavigation();
  return (
    <ScrollView style={styles.container}>
      <Image
        style={styles.profileImage}
        source={{ uri: "https://media-cdn.tripadvisor.com/media/photo-s/19/e8/5e/5f/wave-bar.jpg" }} // Reemplaza con la URL de tu imagen de perfil
      />
      <View style={styles.companyInfoContainer}>
        <Text style={styles.username}>Nombre de la Empresa</Text>
        <Text style={styles.infoText}>Dirección: Calle Principal, Ciudad</Text>
        <Text style={styles.infoText}>Teléfono: +1234567890</Text>
        {/* Otros datos de la empresa */}
      </View>
      <View style={styles.summaryContainer}>
        <Text style={styles.sectionTitle}>Acerca del Establecimiento</Text>
        <Text style={styles.summaryText}>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </Text>
        <TouchableOpacity onPress={() => navigation.navigate("Login")}>
          <Text style={styles.infoText}>Cerrar Session</Text>
        </TouchableOpacity>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
  },
  profileImage: {
    width: "100%",
    height: 200,
    resizeMode: "cover",
  },
  companyInfoContainer: {
    padding: 20,
  },
  username: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 10,
    color:'gray'
  },
  infoText: {
    fontSize: 18,
    marginBottom: 5,
    color:'gray'
  },
  summaryContainer: {
    padding: 20,
    borderTopWidth: 1,
    borderTopColor: "#ccc",
    color:'black'
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 10,
    color:'black'
  },
  summaryText: {
    fontSize: 16,
    color:'gray'
  },
});

export default Profile;
