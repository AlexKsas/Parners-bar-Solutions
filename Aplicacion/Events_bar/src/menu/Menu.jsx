import { createDrawerNavigator } from '@react-navigation/drawer';
import Home from '../components/Home/Home';
import Perfil from '../components/Perfil/Perfil';

const Drawer = createDrawerNavigator();

function Menu() {
  return (
    <Drawer.Navigator>
      <Drawer.Screen name="Inicio" component={Home} />
      <Drawer.Screen name="Perfil" component={Perfil} />
    </Drawer.Navigator>
  );
}
export default Menu;