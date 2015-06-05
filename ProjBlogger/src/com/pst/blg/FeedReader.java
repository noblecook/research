package com.pst.blg;

import java.net.URL;
import java.util.Iterator;
import java.util.List;
import java.io.IOException;
import java.io.InputStreamReader;

import com.sun.syndication.feed.synd.SyndEntry;
import com.sun.syndication.feed.synd.SyndFeed;
import com.sun.syndication.io.SyndFeedInput;
import com.sun.syndication.io.XmlReader;


public class FeedReader {


	public static void main(String[] args) {
		XmlReader xmlRdr = null;
		try {
			URL feedUrl = new URL("http://rss.cnn.com/rss/cnn_topstories.rss");
			xmlRdr = new XmlReader(feedUrl);
			SyndFeedInput input = new SyndFeedInput();
			SyndFeed feed = input.build(xmlRdr); 
			System.out.println("FEED:  " + feed.getEntries().size());

			for (Iterator i = feed.getEntries().iterator(); i.hasNext();) {
				SyndEntry entry = (SyndEntry) i.next();
				System.out.println(entry.getTitle());
			}

		}catch (Exception ex) {
		ex.printStackTrace();
		System.out.println("ERROR: "+ex.getMessage());
		}
		finally {
		if (xmlRdr != null)
			try {
				xmlRdr.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}
