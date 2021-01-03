using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Attitude_script2 : MonoBehaviour
{
    public string[] resMsg;
    public Socket_Comm socket;

    // Start is called before the first frame update
    void Start()
    {
        socket = new Socket_Comm("192.168.0.9", 50007, "attitude");
        socket.Connect();
    }

    // Update is called once per frame
    void Update()
    {
        try
        {
            socket.Request();

            this.transform.rotation = Quaternion.Euler(
                (float)socket.eulerAngles[0],
                (float)socket.eulerAngles[1],
                - (float)socket.eulerAngles[2]
            );
        }
        catch
        {
            socket.Disconnect();
        }
    }
}
