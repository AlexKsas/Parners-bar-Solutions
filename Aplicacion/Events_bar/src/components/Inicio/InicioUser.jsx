const { Image, View, Text, StyleSheet, ScrollView, Dimensions } = require("react-native")
import Carousel from 'react-native-reanimated-carousel';

const InicioUser = () => {
    const width = Dimensions.get('window').width;
		const height = Dimensions.get('window').height;
    const event = [
        {
            id:1,
            nombre: "Rock al parque",
            fecha: "2023-06-15",
            lugar: "Simon Bolivar",
            imagen: "https://colectivosonoro.com/wp-content/uploads/2019/03/rockal25.png"
         }
				,
         {
             id: 2,
             nombre: "Haz Match",
             fecha: "2023-07-22",
             lugar: "Avenida Central 456",
             imagen: "https://www.plans.com.mx/wp-content/uploads/2020/02/perr-1024x1024.jpg"
         },
        // {
        //     "id": "3",
        //     "nombre": "Festival Cordillera",
        //     "fecha": "2023-08-05",
        //     "lugar": "Plaza del Pueblo 789",
        //     "imagen": "https://musicalcedar.com/wp-content/uploads/2023/08/Festival-cordillera-Musical-cedar.png"
        // },
        // {
        //     "id": "4",
        //     "nombre": "Techsound",
        //     "fecha": "2023-09-10",
        //     "lugar": "Calle Secundaria 321",
        //     "imagen": "https://urbanshadows.net/wp-content/uploads/2023/05/Techsound-Fest-foto-de-perfil.jpg"
        // },
        // {
        //     "id": "5",
        //     "nombre": "Estereo Picnic",
        //     "fecha": "2023-10-20",
        //     "lugar": "Avenida Principal 654",
        //     "imagen": "https://colectivosonoro.com/wp-content/uploads/2021/10/festival-estereo-picnic-2022-hori-2.png"
        // },
        // {
        //     "id": "6",
        //     "nombre": "Candelaria Rock",
        //     "fecha": "2023-11-12",
        //     "lugar": "Plaza Central 987",
        //     "imagen": "https://bogota.gov.co/sites/default/files/styles/1050px/public/eventos/2023-08/rock-en-la-media-torta.jpeg"
        // },
        // {
        //     "id": "7",
        //     "nombre": "Monster Of Rock",
        //     "fecha": "2023-12-08",
        //     "lugar": "Calle Principal 147",
        //     "imagen": "https://www.autopistarock.com/images/easyblog_articles/5968/b2ap3_large_PosterMonstersAngraF.jpeg"
        // },
        // {
        //     "id": "8",
        //     "nombre": "Knofest",
        //     "fecha": "2023-09-30",
        //     "lugar": "Avenida Central 258",
        //     "imagen": "https://cdn.puntoticket.com/especiales/knt001_knotfest/img/knotfest-mov-v2.jpg"
        // },
        // {
        //     "id": "9",
        //     "nombre": "Deluxe Night",
        //     "fecha": "2023-07-17",
        //     "lugar": "Plaza del Pueblo 369",
        //     "imagen": "https://www.tropopublicidad.com/fotos/prj_32/2/8/img-28_28-s-1602377193.jpg"
        // },
        // {
        //     "id": "10",
        //     "nombre": "Nigth Party",
        //     "fecha": "2023-08-28",
        //     "lugar": "Calle Secundaria 753",
        //     "imagen": "https://www.tropopublicidad.com/fotos/prj_32/3/2/img-32_32-s-1602377869.jpg"
        // }
    ]

    const renderItem = ({ item }) => (
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
          <Text>{item.content}</Text>
        </View>
      );

      const data = [
        { id: '1', content: 'Contenido 1' },
        { id: '2', content: 'Contenido 2' },
        { id: '3', content: 'Contenido 3' },
        // Agrega más elementos según sea necesario
      ];

    return (
		<ScrollView style={styles.ScrollView}>
				
				{/* {event.map((event) => (
						<View key={event.id} style={styles.container}>
								<Image style={styles.image} source={{ uri: event.imagen }} />
								<View style={styles.textContainer}>
										<Text style={styles.eventName}>{event.nombre}</Text>
										<Text style={styles.eventDate}>{event.fecha}</Text>
								</View>
								<Text style={styles.eventLocation}>{event.lugar}</Text>
						</View>
				))} */}

			<Carousel
				loop
				width={width}
				height={height}
				autoPlay={false}
				vertical
				data={[...new Array(6).keys()]}
				scrollAnimationDuration={1200}
				onSnapToItem={(index) => console.log('current index:', index,  "", event[index])}
				renderItem={( {index} ) => (
					<View
						style={{
							flex: 1,
							borderWidth: 1,
							justifyContent: 'center',
						}}
					>
						<Text style={{ textAlign: 'center', fontSize: 30, color:'black' }}>
							{index}
						</Text>
					</View>
				)}
			/>
		</ScrollView>
    )
}

const styles = StyleSheet.create({
    container: {
        margin: 10,
        padding: 10,
        backgroundColor: 'white',
        borderRadius: 10,
        shadowColor: '#000',
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
        elevation: 5,
    },
    ScrollView:{
        height:'100%',
        width:'100%',
        backgroundColor:'red'
    },
    image: {
        width: '100%',
        height: 200,
        resizeMode: 'cover',
        borderRadius: 8,
    },
    textContainer: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        marginTop: 10,
    },
    eventName: {
        fontSize: 20,
        fontWeight: 'bold',
        color:'gray'
    },
    eventLocation: {
        fontSize: 16,
        color:'gray'
    },
    eventDate: {
        fontSize: 16,
        color:'gray'
    },
})
export default InicioUser