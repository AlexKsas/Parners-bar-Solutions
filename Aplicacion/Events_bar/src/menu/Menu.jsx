import { createDrawerNavigator } from '@react-navigation/drawer';
import Home from '../components/Home/Home';
import Perfil from '../components/Perfil/Perfil';
import SubMenu from './SubMenu'
const Drawer = createDrawerNavigator();

function Menu() {
  return (
    <Drawer.Navigator>
      <Drawer.Screen name="InicioSub" options={{headerShown:false}} component={SubMenu} />
      <Drawer.Screen name="Perfil" component={Perfil} />
    </Drawer.Navigator>
  );
}
export default Menu;