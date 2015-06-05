package com.pst.blg;

import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.security.GeneralSecurityException;
import java.util.Arrays;
import java.util.List;

import com.google.api.client.googleapis.auth.oauth2.GoogleCredential;
import com.google.api.client.http.HttpTransport;
import com.google.api.client.http.javanet.NetHttpTransport;
import com.google.api.client.json.jackson2.JacksonFactory;
import com.google.api.services.blogger.Blogger;
import com.google.api.services.blogger.Blogger.Blogs.Get;
import com.google.api.services.blogger.Blogger.Posts.Insert;
import com.google.api.services.blogger.model.Post;
import com.google.api.services.blogger.model.Post.Blog;


/*
 * Google Blogger Authentication
 * Author:  Patrick Cook
 * Orig Date:  2015-05-30
 * Description:  Logging in to Blogger via API
-------------------------------------------------

The application uses three login methods: 

1.  Username Password:  uses the gdata-blogger-2.0.jar located in gdata-samples
{GData_HOME}\gdata-samples.java-1.47.1\gdata\java\lib

2.  OAuth Token

3.  ClientLogin Authentication

NOTE: The method used is dictated by the constructor

 */

public class Authentication {
	String SERVICENAME = "blogThePlanent-netApp-1";
	String METAFEED_URL = "http://www.blogger.com/feeds/default/blogs";
	String FEED_URI_BASE = "http://www.blogger.com/feeds";
	String POSTS_FEED_URI_SUFFIX = "/posts/default";
	String COMMENTS_FEED_URI_SUFFIX = "/comments/default";
	String next = "https://developers.google.com/oauthplayground";
	String scope = "http://www.blogger.com/feeds/";
	boolean secure = false;
	boolean session = true;
	

	public Authentication()
	{
		
		
		
	}
	
	public GoogleCredential oAuthNLogin()
	{
		//String authSubLogin = AuthSubUtil.getRequestUrl(next, scope, secure, session);
		String BLOG_ID_REAL_TALK = "7645705109247411497";
		String BLOG_ID_CEWPC = "287194822177607500";
		GoogleCredential credential = null;
		String clientID = "838560167308-niq2t1p3av33m9er7vrkutgi1oj3opqi.apps.googleusercontent.com";
		String clientSecret = "DtyVMfWhwEFHuesbsJEvQBD3";
		String refreshToken = "1/alNnLa9mWgIg-IMROlaaYjdnoJuVdRrpfnJKmYbShH0";
		String accessToken ="ya29.hwG92UhoodnGZnO-0PZAVZVx8vKrV0dx5NinRKOe4PvHFuiIm3k-9xo_qVenu1cEKuKnRjZpHJfJ8Q";
		URL FEED_URL;
        try {
			FEED_URL = new URL("http://www.blogger.com/feeds/default/blogs");
		} catch (MalformedURLException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}

        HttpTransport httpTransport = new NetHttpTransport();
        JacksonFactory jsonFactory = new JacksonFactory();
        try {
			credential = new GoogleCredential.Builder()
			        .setTransport(httpTransport)
			        .setJsonFactory(jsonFactory)
			        .setClientSecrets(clientID, clientSecret)
			        .build();
			
			credential.setRefreshToken(refreshToken);
			
		//} catch (Exception e) {
			// TODO Auto-generated catch block
			//e.printStackTrace();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        try {
			credential.refreshToken();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        
        Blogger blogger = new Blogger.Builder(httpTransport, jsonFactory, credential)
        .setApplicationName("Blogger")
        .build();
        
        Get blogGetAction  = null;
        
        // This is the request action that you can configure before sending the request.
        try {
			 blogGetAction = blogger.blogs().get(BLOG_ID_REAL_TALK);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        
        // Restrict the result content to just the data we need.
        blogGetAction.setFields("description,name,posts/totalItems,updated");

        // This step sends the request to the server.
        com.google.api.services.blogger.model.Blog blog = null;
		try {
			blog = blogGetAction.execute();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

        // Now we can navigate the response.
        System.out.println("Name: "+blog.getName());
        System.out.println("App Name: " + blogger.getRootUrl() );
        
        // Construct a post to insert
        Post content = new Post();
        content.setTitle("A test post to Remember2");
        content.setContent("With <b>HTML</b> content");
        
        
     // The request action.
        Insert postsInsertAction = null;
		try {
			postsInsertAction = blogger.posts()
			        .insert(BLOG_ID_REAL_TALK, content);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

        // Restrict the result content to just the data we need.
        postsInsertAction.setFields("author/displayName,content,published,title,url");

        // This step sends the request to the server.
        Post post = null;
		try {
			post = postsInsertAction.execute();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

        // Now we can navigate the response.
        System.out.println("Title: " + post.getTitle());
        System.out.println("Author: " + post.getAuthor().getDisplayName());
        System.out.println("Published: " + post.getPublished());
        System.out.println("URL: " + post.getUrl());
        System.out.println("Content: " + post.getContent());

		return credential;
	}
		
}
