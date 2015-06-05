package com.pst.blg;

import static org.junit.Assert.*;

import org.junit.Test;

public class TestSpecialtyPost {

	@Test
	public void testPingTest() {
		SpecialtyPost tsp = new SpecialtyPost();
		String result = tsp.pingTest();
        assertEquals("Ping", result);		
	}
	

}
