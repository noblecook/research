package com.pst.blg;

import com.google.api.client.googleapis.auth.oauth2.GoogleCredential;


/*
 * Client user name and password is no longer supported
 * https://developers.google.com/identity/protocols/OAuth2
 * https://developers.google.com/api-client-library/java/google-api-java-client/oauth2
 * 
 */
public class GoogleBloggerDriver {
	private static String fileLocation = 
			"C:/Users/patri_000/workspace/ProjBlogger/conf/config.properties";
	
	
	public static void main(String[] args)
	{
		BloggerUtility blgUtil = new BloggerUtility(fileLocation);
		Authentication authN = new Authentication();
		authN.oAuthNLogin();
	}
}
