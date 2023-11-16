import React from "react";
<<<<<<< Updated upstream
import { StyleSheet, Text, View, Image, ScrollView } from "react-native";

const Profile = () => {
=======
import { StyleSheet, Text, View, Image, ScrollView, TouchableOpacity } from "react-native";
import { useNavigation } from '@react-navigation/native';

const Perfil = () => {
  const navigation = useNavigation();
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
=======
        <TouchableOpacity style={styles.cerrarsesions} onPress={() => navigation.navigate('Login')}>
          <Text style={styles.sectionTitlec}>Cerrar Sesion</Text>
        </TouchableOpacity>
>>>>>>> Stashed changes
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
  },
<<<<<<< Updated upstream
=======
  cerrarsesions:{
    height:50,
    width:300,
    backgroundColor:'#094293',
    borderRadius:30,
    paddingHorizontal:'25%',
    paddingVertical:'2%',
    marginTop:10,
    marginHorizontal:'7%'
  },
>>>>>>> Stashed changes
  profileImage: {
    width: "100%",
    height: 200,
    resizeMode: "cover",
  },
  companyInfoContainer: {
    padding: 20,
  },
  username: {
<<<<<<< Updated upstream
=======
    color:"gray",
>>>>>>> Stashed changes
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 10,
  },
  infoText: {
    fontSize: 18,
    marginBottom: 5,
<<<<<<< Updated upstream
=======
    color:'gray'
>>>>>>> Stashed changes
  },
  summaryContainer: {
    padding: 20,
    borderTopWidth: 1,
    borderTopColor: "#ccc",
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 10,
<<<<<<< Updated upstream
=======
    color:'gray'
  },
  sectionTitlec:{
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 10,
    color:'white'
>>>>>>> Stashed changes
  },
  summaryText: {
    fontSize: 16,
    color: "#666",
  },
});

<<<<<<< Updated upstream
export default Profile;
=======
export default Perfil;
>>>>>>> Stashed changes
