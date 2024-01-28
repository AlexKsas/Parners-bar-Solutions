import Geolocation from '@react-native-community/geolocation';
import React, { Component, PureComponent } from 'react'
import { View, StyleSheet, AppRegistry,
  Text,
  ScrollView,
  Animated,
  Image,
  Dimensions, 
  TouchableOpacity} from 'react-native';
import MapView, { Marker } from 'react-native-maps';


const Images = [
  { uri: "https://i.imgur.com/sNam9iJ.jpg" },
  { uri: "https://i.imgur.com/N7rlQYt.jpg" },
  { uri: "https://i.imgur.com/UDrH0wm.jpg" },
  { uri: "https://i.imgur.com/Ka8kNST.jpg" },
];

const { width, height } = Dimensions.get("window");

const CARD_HEIGHT = height / 4;
const CARD_WIDTH = CARD_HEIGHT - 10;
const SPACING_FOR_CARD_INSET = width * 0.10 - 10;


class Maps extends Component  {
  
  constructor(){
    super()
    
    this.state={  
      ubicacion: '',
      longitude:'',
      latitude:''
    }
  }

   async componentDidUpdate () {
    await Geolocation.getCurrentPosition(
      info => {
        this.setState({
          longitude:info.coords.longitude,
          latitude:info.coords.latitude
        })
        // setGeo({
        //   lat: info.coords.latitude,
        //   long: info.coords.longitude,
        // });
        console.log(info.coords.latitude + '#' + info.coords.longitude);  
      },
      error => console.log(error),
      {
        enableHighAccuracy: false,
        timeout: 20000,
        maximumAge: 10,
        distanceFilter: 0,
      },
    );
  };

  render(){
    return (
      <View style={styles.ViewPrincipal}>
        <MapView style={styles.maps}
          initialRegion={{
            latitude: 4.5385391,
            longitude: -74.1133762,
            latitudeDelta: 0.0922,
            longitudeDelta: 0.0421,
          }}
        >
          <Marker
            coordinate={{
            latitude: 4.5385391,
            longitude: -74.1133762
            }}
            title="Aqui estoy perro hp"
            description="esta es mi casa"
            />
        </MapView>
              
              <Animated.ScrollView
                horizontal
                pagingEnabled
                scrollEventThrottle={1}
                snapToInterval={CARD_WIDTH + 20}
                style={styles.scrollView}
                snapToAlignment="center"
                contentInset={{
                  top: 0,
                  left: SPACING_FOR_CARD_INSET,
                  bottom: 0,
                  right: SPACING_FOR_CARD_INSET
                }}
                contentContainerStyle={{
                  paddingHorizontal: Platform.OS === 'android' ? SPACING_FOR_CARD_INSET : 0
                }}
              >
                <View style={styles.card}>
                  <Text style={{color:'red'}}>Aqui estoy perro hp</Text>
                </View>
              
              </Animated.ScrollView>
        <TouchableOpacity onPress={this.encontrarCoordenadas}>
          <Text >Donde Estoy?</Text>
          <Text>Ubicación: {this.state.ubicacion}</Text>
        </TouchableOpacity>
      </View>
    )
  }
  
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  viewComponent:{
    backgroundColor:'white',
    width:'100%'
  },
  scrollView: {
    position: "absolute",
    bottom: 30,
    left: 0,
    right: 0,
    paddingVertical: 10,
  },
  endPadding: {
    paddingRight: width - CARD_WIDTH,
  },
  card: {
    padding: 10,
    elevation: 2,
    backgroundColor: "#FFF",
    marginHorizontal: 10,
    shadowColor: "#000",
    shadowRadius: 5,
    shadowOpacity: 0.3,
    shadowOffset: { x: 2, y: -2 },
    height: CARD_HEIGHT,
    width: CARD_WIDTH,
    overflow: "hidden",
  },
  cardImage: {
    flex: 3,
    width: "100%",
    height: "100%",
    alignSelf: "center",
  },
  textContent: {
    flex: 1,
  },
  cardtitle: {
    fontSize: 12,
    marginTop: 5,
    fontWeight: "bold",
  },
  cardDescription: {
    fontSize: 12,
    color: "#444",
  },
  markerWrap: {
    alignItems: "center",
    justifyContent: "center",
  },
  marker: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: "rgba(130,4,150, 0.9)",
  },
  ring: {
    width: 24,
    height: 24,
    borderRadius: 12,
    backgroundColor: "rgba(130,4,150, 0.3)",
    position: "absolute",
    borderWidth: 1,
    borderColor: "rgba(130,4,150, 0.5)",
  },
  absoluteFillObject:{

  },
  maps:{
    // margin:'5%',
    height:'100%',
    width:'100%'
  },
  ViewPrincipal:{
    flex:1,
    height:'100%',
    width:'100%'
  },
  scrollView: {
    position: "absolute",
    bottom: 0,
    left: 0,
    right: 0,
    paddingVertical: 10,
  },
  card:{
    elevation: 2,
    backgroundColor: "#FFF",
    borderTopLeftRadius: 5,
    borderTopRightRadius: 5,
    marginHorizontal: 10,
    shadowColor: "#000",
    shadowRadius: 5,
    shadowOpacity: 0.3,
    shadowOffset: { x: 2, y: -2 },
    height: CARD_HEIGHT,
    width: CARD_WIDTH,
    overflow: "hidden",
  }

})
export default Maps