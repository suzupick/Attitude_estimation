using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class Socket_Comm
{
    public string ip_adr;
    public int port;
    public string sendMsg;
    public System.Net.Sockets.TcpClient tcp;
    public System.Net.Sockets.NetworkStream ns;
    public string[] resMsg_split = new string[3];
    public double[] eulerAngles = new double[3];
    public static double PI = 3.14159265358979;

    public Socket_Comm(string ip_adr, int port, string sendMsg)
    {
        this.ip_adr = ip_adr;
        this.port = port;
        this.sendMsg = sendMsg;
    }

    public void Connect()
    {
        this.tcp = new System.Net.Sockets.TcpClient(this.ip_adr, this.port);
        this.ns = this.tcp.GetStream();

        Debug.Log(string.Format("サーバー({0}:{1})と接続しました({2}:{3})。",
            ((System.Net.IPEndPoint)tcp.Client.RemoteEndPoint).Address,
            ((System.Net.IPEndPoint)tcp.Client.RemoteEndPoint).Port,
            ((System.Net.IPEndPoint)tcp.Client.LocalEndPoint).Address,
            ((System.Net.IPEndPoint)tcp.Client.LocalEndPoint).Port));

        this.ns.ReadTimeout = 10000;
        this.ns.WriteTimeout = 10000;
    }

    public void Request()
    {
        System.Text.Encoding enc = System.Text.Encoding.UTF8;
        byte[] sendBytes = enc.GetBytes(sendMsg);

        ns.Write(sendBytes, 0, sendBytes.Length);
        Debug.Log(sendMsg);


        System.IO.MemoryStream ms = new System.IO.MemoryStream();
        byte[] resBytes = new byte[256];
        int resSize = 0;
        do
        {
            resSize = ns.Read(resBytes, 0, resBytes.Length);

            if (resSize == 0)
            {
                Debug.Log("サーバーが切断しました。");
                break;
            }

            ms.Write(resBytes, 0, resSize);

        } while (ns.DataAvailable);

        string resMsg = enc.GetString(ms.GetBuffer(), 0, (int)ms.Length);
        ms.Close();

        Debug.Log(resMsg);

        // \r\nでスプリット
        string[] separator = new string[] { "\n" };
        resMsg_split = resMsg.Split(separator, StringSplitOptions.None);

        // Debug.Log(resMsg_split[0]);
        // Debug.Log(resMsg_split[1]);
        // Debug.Log(resMsg_split[2]);

        this.eulerAngles[0] = Convert.ToDouble(resMsg_split[0]) / PI * 180;
        this.eulerAngles[1] = Convert.ToDouble(resMsg_split[1]) / PI * 180;
        this.eulerAngles[2] = Convert.ToDouble(resMsg_split[2]) / PI * 180;

        //Debug.Log("OK");
    }

    public void Disconnect()
    {
        this.ns.Close();
        this.tcp.Close();
        Debug.Log("切断しました。");
    }

}