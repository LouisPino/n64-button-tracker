{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 5,
			"revision" : 4,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 84.0, 144.0, 640.0, 480.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"assistshowspatchername" : 0,
		"boxes" : [ 			{
				"box" : 				{
					"basictuning" : 440,
					"clipheight" : 20.0,
					"data" : 					{
						"clips" : [ 							{
								"absolutepath" : "bd+hh.aiff",
								"filename" : "bd+hh.aiff",
								"filekind" : "audiofile",
								"id" : "u020005126",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Clap 01.wav",
								"filename" : "Clap 01.wav",
								"filekind" : "audiofile",
								"id" : "u513004595",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Bonus Scoring.wav",
								"filename" : "Bonus Scoring.wav",
								"filekind" : "audiofile",
								"id" : "u845005628",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Bonus Scoring 2.wav",
								"filename" : "Bonus Scoring 2.wav",
								"filekind" : "audiofile",
								"id" : "u199005692",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Click Whoosh.wav",
								"filename" : "Click Whoosh.wav",
								"filekind" : "audiofile",
								"id" : "u370005744",
								"loop" : 0,
								"content_state" : 								{

								}

							}
, 							{
								"absolutepath" : "Fox - Item Grab.wav",
								"filename" : "Fox - Item Grab.wav",
								"filekind" : "audiofile",
								"id" : "u293005792",
								"loop" : 0,
								"content_state" : 								{

								}

							}
 ]
					}
,
					"followglobaltempo" : 0,
					"formantcorrection" : 0,
					"id" : "obj-20",
					"maxclass" : "playlist~",
					"mode" : "basic",
					"numinlets" : 1,
					"numoutlets" : 5,
					"originallength" : [ 0.0, "ticks" ],
					"originaltempo" : 120.0,
					"outlettype" : [ "signal", "signal", "signal", "", "dictionary" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 89.0, 261.0, 191.0, 93.0 ],
					"pitchcorrection" : 0,
					"quality" : "basic",
					"timestretch" : [ 0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-14",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 89.0, 229.0, 56.0, 22.0 ],
					"text" : "r triggers"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-11",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 0,
					"patching_rect" : [ 60.0, 120.0, 209.0, 22.0 ],
					"text" : "MUGIC_Percussion_Jasmine.maxpat"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 333.0, 101.0, 47.0, 22.0 ],
					"text" : "zl nth 6"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-2",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 333.0, 62.0, 71.0, 22.0 ],
					"text" : "r mugicdata"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-1",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 467.0, 341.0, 55.0, 22.0 ],
					"text" : "dac~ 1 2"
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-20", 0 ],
					"source" : [ "obj-14", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 0 ],
					"source" : [ "obj-2", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 1 ],
					"order" : 0,
					"source" : [ "obj-20", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 0 ],
					"order" : 1,
					"source" : [ "obj-20", 0 ]
				}

			}
 ],
		"parameters" : 		{
			"obj-11::obj-100::obj-18" : [ "number[3]", "number[1]", 0 ],
			"obj-11::obj-141::obj-18" : [ "number[4]", "number[1]", 0 ],
			"obj-11::obj-1::obj-76" : [ "live.text[2]", "live.text[1]", 0 ],
			"obj-11::obj-248" : [ "number", "number", 0 ],
			"parameterbanks" : 			{
				"0" : 				{
					"index" : 0,
					"name" : "",
					"parameters" : [ "-", "-", "-", "-", "-", "-", "-", "-" ]
				}

			}
,
			"inherited_shortname" : 1
		}
,
		"dependency_cache" : [ 			{
				"name" : "Bonus Scoring 2.wav",
				"bootpath" : "~/Code/n64/samples/Smash64Samples",
				"patcherrelativepath" : "../samples/Smash64Samples",
				"type" : "WAVE",
				"implicit" : 1
			}
, 			{
				"name" : "Bonus Scoring.wav",
				"bootpath" : "~/Code/n64/samples/Smash64Samples",
				"patcherrelativepath" : "../samples/Smash64Samples",
				"type" : "WAVE",
				"implicit" : 1
			}
, 			{
				"name" : "Clap 01.wav",
				"bootpath" : "C74:/packages/MaxIntroLessons/media",
				"type" : "WAVE",
				"implicit" : 1
			}
, 			{
				"name" : "Click Whoosh.wav",
				"bootpath" : "~/Code/n64/samples/Smash64Samples",
				"patcherrelativepath" : "../samples/Smash64Samples",
				"type" : "WAVE",
				"implicit" : 1
			}
, 			{
				"name" : "Fox - Item Grab.wav",
				"bootpath" : "~/Code/n64/samples/Smash64Samples",
				"patcherrelativepath" : "../samples/Smash64Samples",
				"type" : "WAVE",
				"implicit" : 1
			}
, 			{
				"name" : "Herve_serial.js",
				"bootpath" : "~/Documents/Cichorium/YouInMind/elements/Scintillation",
				"patcherrelativepath" : "../../../Documents/Cichorium/YouInMind/elements/Scintillation",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "MUGIC_Connect.maxpat",
				"bootpath" : "~/Documents/Cichorium/YouInMind/elements/Scintillation",
				"patcherrelativepath" : "../../../Documents/Cichorium/YouInMind/elements/Scintillation",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "MUGIC_Percussion_Jasmine.maxpat",
				"bootpath" : "~/Documents/Cichorium/YouInMind/elements/Scintillation",
				"patcherrelativepath" : "../../../Documents/Cichorium/YouInMind/elements/Scintillation",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "OSC-route.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "OpenSoundControl.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "bd+hh.aiff",
				"bootpath" : "C74:/docs/tutorial-patchers/msp-tut",
				"type" : "AIFF",
				"implicit" : 1
			}
, 			{
				"name" : "fixed_accel.js",
				"bootpath" : "~/Documents/Cichorium/YouInMind/elements/Scintillation",
				"patcherrelativepath" : "../../../Documents/Cichorium/YouInMind/elements/Scintillation",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "fixed_gyro.js",
				"bootpath" : "~/Documents/Cichorium/YouInMind/elements/Scintillation",
				"patcherrelativepath" : "../../../Documents/Cichorium/YouInMind/elements/Scintillation",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "fixed_mag.js",
				"bootpath" : "~/Documents/Cichorium/YouInMind/elements/Scintillation",
				"patcherrelativepath" : "../../../Documents/Cichorium/YouInMind/elements/Scintillation",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "fixed_quat.js",
				"bootpath" : "~/Documents/Cichorium/YouInMind/elements/Scintillation",
				"patcherrelativepath" : "../../../Documents/Cichorium/YouInMind/elements/Scintillation",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "quat_to_euler.js",
				"bootpath" : "~/Documents/Cichorium/YouInMind/elements/Scintillation",
				"patcherrelativepath" : "../../../Documents/Cichorium/YouInMind/elements/Scintillation",
				"type" : "TEXT",
				"implicit" : 1
			}
 ],
		"autosave" : 0
	}

}
