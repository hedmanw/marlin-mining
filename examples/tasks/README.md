# Performing tasks in INCLINE VM
This section describes the actions to run the test environments and perform some rudimentary actions in the editors.

## Manual unstructured merging in RCPTT/ECLIPSE CDT
We use [Eclipse CDT](http://www.eclipse.org/cdt/) to launch inside RCPTT, this will be referred to as the AUT (application under test), since RCPTT is really a testing tool.

Start:
1. Launch RCPTT from the VM desktop. Use the default workspace if prompted.
2. Open the "IntegrationTask" test case from the file tree.
3. At the bottom panel, in the "Applications" tab, right click "org.eclipse.epp.package.cpp.product", and select "Run". Save any changes to files. The AUT will be launched.
4. An empty instance of Eclipse CDT will open. Follow the instructions below to populate the preconfigured workspace and record your actions.

Recording actions in the AUT:
1. Ensure that the AUT is running through RCPTT, as above.
2. In the RCPTT instance, open your test case. In the upper left, there is a "Record" button. Press it to start recording.
3. The RCPTT instance will minimize, and actions you make in the AUT are recorded. The workspace is populated with task files in the directories `busybox` and `vim`.
4. To stop recording, press the red square in the RCPTT instance.

Example merging [Taken from here.](http://stackoverflow.com/questions/4623564/how-do-i-compare-two-files-using-eclipse-is-there-any-option-provided-by-eclips):

1. Start recording as above.
2. Select the mainline file and the clone file you want to merge.
3. Right click and select Compare With -> Each other.
4. A two-way diff view is opened. The files can be swapped from left to right if they are on the opposite side.
5. As soon as you start with the task, please also manually record the time required to complete the task.
6. Perform the editing as instructed in the task. The diff view is editable, use it (copy-pasteing etc) to manipulate the `mainline` with changes from the `fork`.
7. When the task is finished, stop recording and save the script so we can analyze the edit operations. Also stop counting the time.
8. Save the result file(s) so we can compare the outcome. (Somewhere outside the AUT, since it will be lost otherwise.)
9. Report back the elapsed time, the script content, and the result file(s).

## MPS
1. Launch MPS from the VM desktop.
2. Open the integrated files in Examples/Examples/Imported2/.
3. To open the four quadrants of views, use the menu Tools > Arrange Views (Ctrl + Alt + Shift + V)
4. To navigate between chunks inside the views, use the menu Tools > Next chunk (Ctrl + Alt + Shift + Left Arrow) / Previous chunk (Ctrl + Alt + Shift + Right Arrow)
5. To apply intentions, select nodes in a view (using Shift + Arrow Up/Down), use menu Tools to find the intention you want.
6. Execute intentions: Tools > Commit intentions
7. Export result: Tools > Export C++ File

# Creating environments in INCLINE VM
This section describes how to setup the test environments in the VM -- uninteresting if you're just evaluating the VM :).

## Eclipse
The setup instructions are shown [here](https://www.youtube.com/watch?v=prXLW38mk8g) if you prefer a video. Point 6 is not included in the video though.

1. Download Eclipse [RCPTT](http://www.eclipse.org/rcptt/download/).
2. Launch RCPTT
3. Select a workspace for RCPTT
4. Create a new project under File -> New -> RCP Testing Tool Project
5. After the project is created, open the "Project Settings" file. Under "Default Contexts", create a new Workspace which will be used by the AUT.
6. The new Workspace context file will be opened, in this, create a new project and import the directories in `tasks/`. Tick the "Clear workspace" checkbox.
7. In the project, create a new "Test case" by New -> Test case. The new test case definition file will be opened.
8. In the "Applications panel", at the bottom of the screen, right click and select "New...". You will be prompted to point to an Eclipse installation (i.e. your Eclipse CDT installation).
9. This new application will be added to the same panel. Right click it, and select "Run". Save any changes to files. The AUT will be launched.

## MPS
1. Build the jar in ppmerge:astmerge using `mvn compile assembly:single`
2. Run the jar on two input variants `java -jar astmerge-1.0-SNAPSHOT-jar-with-dependencies.jar MAINLINE_SOURCE VARIANT_SOURCE OUTPUT_INTEGRATED`
3. scp the output onto the vm `scp -P 3022 OUTPUT_INTEGRATED incline@127.0.0.1:`
4. Import in into MPS with Tools > Import CPP