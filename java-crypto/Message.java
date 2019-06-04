import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.nio.file.Files;
import java.security.InvalidKeyException;
import java.security.KeyFactory;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.Signature;
import java.security.spec.PKCS8EncodedKeySpec;
import java.util.ArrayList;
import java.util.List;
import java.security.cert.Certificate;

import javax.swing.JOptionPane;

public class Message {
	private List<byte[]> list;
	
	//The constructor of Message class builds the list that will be written to the file. 
	//The list consists of the message and the signature.
	public Message(String data, String keyFile) throws InvalidKeyException, Exception {
		list = new ArrayList<byte[]>();
		list.add(data.getBytes());
		list.add(sign(data, keyFile));
	}
	
	//The method that signs the data using the private key that is stored in keyFile path
	public byte[] sign(String data, String keyFile) throws InvalidKeyException, Exception{
		Signature rsa = Signature.getInstance("SHA1withRSA"); 
		rsa.initSign(getPrivate(keyFile));
		rsa.update(data.getBytes());
		return rsa.sign();
	}
	
	//Method to retrieve the Private Key from a file
	public PrivateKey getPrivate(String filename) throws Exception {
		byte[] keyBytes = Files.readAllBytes(new File(filename).toPath());
		PKCS8EncodedKeySpec spec = new PKCS8EncodedKeySpec(keyBytes);
		KeyFactory kf = KeyFactory.getInstance("RSA");
		return kf.generatePrivate(spec);
	}

	//Method to retrieve the Public Key from a file
	public PublicKey getPublic(String filename) throws Exception {
		byte[] keyBytes = Files.readAllBytes(new File(filename).toPath());
		PKCS8EncodedKeySpec spec = new PKCS8EncodedKeySpec(keyBytes);
		KeyFactory kf = KeyFactory.getInstance("RSA");
		return kf.generatePublic(spec);
	}
	
	//Method to write the List of byte[] to a file
	private void writeToFile(String filename) throws FileNotFoundException, IOException {
		File f = new File(filename);
		f.getParentFile().mkdirs();
		ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(filename));
	    out.writeObject(list);
		out.close();
		System.out.println("Your file is ready.");
	}
	
	public static void main(String[] args) throws InvalidKeyException, IOException, Exception{
		String data = JOptionPane.showInputDialog("Type your message here");
		
		Message msg = new Message(data, "KeyPair/privateKey").writeToFile("MyData/SignedData.txt");
		byte[] bdata = data.getBytes();
		byte[] sigdata = new byte[msg.list.size()];
		msg.list.toArray(sigdata);	//(byte[])msg.list.toArray();

		Signature rsa = Signature.getInstance("SHA1withRSA");
		PublicKey pub = Message.getPublic("KeyPair/publicKey");
		rsa.initVerify(pub);

		rsa.update(bdata);
		boolean verified = rsa.verify(sigdata);
		System.out.println("Verified: " + verified);

	}
}
