
import React, { Component } from 'react'
import {
    GoogleSignin,
    GoogleSigninButton,
    statusCodes,
  } from '@react-native-google-signin/google-signin';

  GoogleSignin.configure({
    scopes: ['email'], // what API you want to access on behalf of the user, default is email and profile
    webClientId:
      '367568135817-navvj8ldq6l6324v9ga5gu07c6d378ct.apps.googleusercontent.com', // client ID of type WEB for your server (needed to verify user ID and offline access)
    offlineAccess: true, // if you want to access Google API on behalf of the user FROM YOUR SERVER
  });
export default class GoogleSigIng extends Component {
    constructor(){
        super()
        this.state={
            isSigninInProgress:false
        }
    }
    
    signIn = async () => {
        try {
          await GoogleSignin.hasPlayServices();
          const userInfo = await GoogleSignin.signIn();
          setState({ userInfo });
        } catch (error) {
          if (error.code === statusCodes.SIGN_IN_CANCELLED) {
            console.log("error ", error)
          } else if (error.code === statusCodes.IN_PROGRESS) {
            console.log("error ", error)
            
          } else if (error.code === statusCodes.PLAY_SERVICES_NOT_AVAILABLE) {
            console.log("error ", error)
            
          } else {
            console.log("error ", error)
          }
        }
      };
  render() {
    return (
        <GoogleSigninButton
            size={GoogleSigninButton.Size.Standard}
            color={GoogleSigninButton.Color.Light}
            onPress={this.signIn}
            testID='Ingresar Con Google'
            disabled={this.state.isSigninInProgress}
        />
    )
  }
}
