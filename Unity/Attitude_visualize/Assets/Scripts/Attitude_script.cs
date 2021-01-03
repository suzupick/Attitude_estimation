using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Text;
using System.IO;
using System;

public class Attitude_script : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        string sendMsg = "attitude";
        string ipOrHost = "192.168.0.9";
        int port = 50007;


        System.Net.Sockets.TcpClient tcp = new System.Net.Sockets.TcpClient(ipOrHost, port);
        
        Debug.Log(string.Format("サーバー({0}:{1})と接続しました({2}:{3})。",
                ((System.Net.IPEndPoint)tcp.Client.RemoteEndPoint).Address,
                ((System.Net.IPEndPoint)tcp.Client.RemoteEndPoint).Port,
                ((System.Net.IPEndPoint)tcp.Client.LocalEndPoint).Address,
                ((System.Net.IPEndPoint)tcp.Client.LocalEndPoint).Port));

        System.Net.Sockets.NetworkStream ns = tcp.GetStream();

        ns.ReadTimeout = 10000;
        ns.WriteTimeout = 10000;

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
        string[] resMsg_split = resMsg.Split(separator, StringSplitOptions.None);

        Debug.Log(resMsg_split[0]);
        // Debug.Log(resMsg_split[1]);
        // Debug.Log(resMsg_split[2]);

        ns.Close();
        tcp.Close();
        Debug.Log("切断しました。");

    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
