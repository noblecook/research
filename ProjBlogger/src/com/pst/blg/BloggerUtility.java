package com.pst.blg;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.URL;
import java.util.Properties;


public class BloggerUtility {
	
	private String username;
	private String password;
	private String serviceName;
	private String METAFEED_URL;
	private String FEED_URI_BASE;
	private String POSTS_FEED_URI_SUFFIX;
	private String COMMENTS_FEED_URI_SUFFIX;
	
	public BloggerUtility(String propertiesFile)
	{
		File file = new File(propertiesFile);
		FileInputStream fileInput = null;
		try {
			fileInput = new FileInputStream(file);
		} catch (FileNotFoundException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		Properties props = new Properties();
		try {
			props.load(fileInput);
			fileInput.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		this.setUsername(props.getProperty("USERNAME"));
		this.setPassword(props.getProperty("PASSWORD"));
		this.setServiceName(props.getProperty("SERVICENAME"));
		this.setMETAFEED_URL(props.getProperty("METAFEED_URL"));
		this.setFEED_URI_BASE(props.getProperty("FEED_URI_BASE"));
		this.setPOSTS_FEED_URI_SUFFIX(props.getProperty("POSTS_FEED_URI_SUFFIX"));
		this.setCOMMENTS_FEED_URI_SUFFIX(props.getProperty("COMMENTS_FEED_URI_SUFFIX"));
		
	}

	
	public String getUsername() {
		return username;
	}



	public void setUsername(String username) {
		this.username = username;
	}



	public String getPassword() {
		return password;
	}



	public void setPassword(String password) {
		this.password = password;
	}



	public String getServiceName() {
		return serviceName;
	}



	public void setServiceName(String serviceName) {
		this.serviceName = serviceName;
	}



	public String getMETAFEED_URL() {
		return METAFEED_URL;
	}



	public void setMETAFEED_URL(String mETAFEED_URL) {
		METAFEED_URL = mETAFEED_URL;
	}



	public String getFEED_URI_BASE() {
		return FEED_URI_BASE;
	}



	public void setFEED_URI_BASE(String fEED_URI_BASE) {
		FEED_URI_BASE = fEED_URI_BASE;
	}



	public String getPOSTS_FEED_URI_SUFFIX() {
		return POSTS_FEED_URI_SUFFIX;
	}



	public void setPOSTS_FEED_URI_SUFFIX(String pOSTS_FEED_URI_SUFFIX) {
		POSTS_FEED_URI_SUFFIX = pOSTS_FEED_URI_SUFFIX;
	}



	public String getCOMMENTS_FEED_URI_SUFFIX() {
		return COMMENTS_FEED_URI_SUFFIX;
	}



	public void setCOMMENTS_FEED_URI_SUFFIX(String cOMMENTS_FEED_URI_SUFFIX) {
		COMMENTS_FEED_URI_SUFFIX = cOMMENTS_FEED_URI_SUFFIX;
	}



	
}
